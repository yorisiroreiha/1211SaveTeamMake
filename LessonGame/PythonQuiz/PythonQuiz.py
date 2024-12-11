import json
import tkinter as tk
from tkinter import messagebox
import random

# JSON形式のクイズデータを読み込む
with open('quiz_questions.json', 'r', encoding='utf-8') as f:
    quiz_questions = json.load(f)

def get_random_questions(quiz_questions, num_questions):
    all_questions = quiz_questions
    random.shuffle(all_questions)
    return all_questions[:num_questions]

def quiz():
    score = 0
    questions = get_random_questions(quiz_questions, 20)  # ランダムに20問取得

    for q in questions:
        options = q["options"]
        random.shuffle(options)  # 選択肢をランダムに並べ替え
        correct_answer = q["answer"]

        print(q["question"])
        for i, option in enumerate(options, 1):
            print(f"{i}) {option}")

        user_answer = input("回答番号を入力してください: ")
        if options[int(user_answer) - 1] == correct_answer:
            print("正解！")
            score += 1
        else:
            print("不正解。")

    print(f"\nあなたのスコアは {score}/20 です。")

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python 基礎文法クイズ")

        self.questions = self.get_random_questions(quiz_questions, 20)  # クイズの質問数を20に設定
        self.current_question = 0
        self.score = 0
        self.wrong_answers = []

        self.question_label = tk.Label(root, text=self.questions[self.current_question]['question'], font=("Arial", 20), wraplength=600, height=5)
        self.question_label.pack(pady=20)

        self.option_buttons = []
        for i in range(3):
            btn = tk.Button(root, text=self.questions[self.current_question]['options'][i], font=("Arial", 18), width=50, wraplength=400, bg="lightblue", command=lambda b=i: self.check_answer(b))
            btn.pack(pady=10)
            self.option_buttons.append(btn)

    def get_random_questions(self, quiz_questions, num_questions):
        all_questions = [q for q in quiz_questions]
        random.shuffle(all_questions)
        return all_questions[:num_questions]

    def check_answer(self, chosen_option):
        if self.option_buttons[chosen_option].cget('text') == self.questions[self.current_question]['answer']:
            self.score += 1
        else:
            self.wrong_answers.append({
                "question": self.questions[self.current_question]['question'], 
                "chosen": self.option_buttons[chosen_option].cget('text'), 
                "correct": self.questions[self.current_question]['answer'],
                "explanation": self.questions[self.current_question]['explanation']
            })

        self.current_question += 1
        if self.current_question < len(self.questions):
            self.update_question()
        else:
            self.show_score()

    def update_question(self):
        question = self.questions[self.current_question]
        self.question_label.config(text=question['question'])
        options = question['options']
        random.shuffle(options)
        for i, btn in enumerate(self.option_buttons):
            btn.config(text=options[i])

    def show_score(self):
        result_text = f"あなたのスコアは {self.score}/{len(self.questions)} です\n\n"
        if self.wrong_answers:
            result_text += "不正解だった問題:\n"
            for wa in self.wrong_answers:
                result_text += f"問題: {wa['question']}\n選択した答え: {wa['chosen']}\n正しい答え: {wa['correct']}\n解説: {wa['explanation']}\n\n"
        messagebox.showinfo("結果", result_text)
        self.root.quit()

if __name__ == "__main__":
    main_root = tk.Tk()
    app = QuizApp(main_root)
    main_root.mainloop()
