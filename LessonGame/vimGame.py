# -*- coding: utf-8 -*-
import tkinter as tk
import random

class VimPracticeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("中級者向けVim練習ゲーム")
        self.root.geometry("800x400")
        self.root.config(bg="#f0f0f0")

        self.score = 0
        self.streak = 0  # 正解の連続数を記録
        self.time_left = 15

        self.root.bind("<Configure>", self.resize_text)

        main_frame = tk.Frame(root, bg="#f0f0f0")
        main_frame.pack(fill=tk.BOTH, expand=True)

        left_frame = tk.Frame(main_frame, bg="#f0f0f0")
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.task_label = tk.Label(left_frame, text="Enterキーを押してゲームを開始してください", font=("Helvetica", 14), bg="#ffffff", bd=2, relief="groove")
        self.task_label.pack(pady=20, fill=tk.BOTH, expand=True)

        self.entry = tk.Entry(left_frame, font=("Helvetica", 14), justify="center")
        self.entry.pack(pady=20, ipadx=10)
        self.entry.bind("<Return>", self.start_game)

        status_frame = tk.Frame(left_frame, bg="#f0f0f0")
        status_frame.pack(pady=10)

        self.score_label = tk.Label(status_frame, text=f"スコア: {self.score}", font=("Helvetica", 12), bg="#f0f0f0")
        self.score_label.pack(side=tk.LEFT, padx=10)

        self.timer_label = tk.Label(status_frame, text=f"残り時間: {self.time_left}秒", font=("Helvetica", 12), bg="#f0f0f0")
        self.timer_label.pack(side=tk.RIGHT, padx=10)

        right_frame = tk.Frame(main_frame, bg="#f0f0f0", bd=2, relief="groove")
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.command_list1 = tk.Label(right_frame, text="カーソルを右に移動: l\n"
                                                       "カーソルを左に移動: h\n"
                                                       "カーソルを上に移動: k\n"
                                                       "カーソルを下に移動: j\n"
                                                       "単語移動（次）: w\n"
                                                       "単語移動（前）: b\n"
                                                       "行全体削除: dd\n"
                                                       "複数行挿入: o\n"
                                                       "現在の単語削除: dw\n"
                                                       "単語末尾移動: e\n"
                                                       "行の先頭に移動: 0\n"
                                                       "行の末尾に移動: $\n"
                                                       "テキストを挿入: i\n"
                                                       "テキストを削除: x\n",
                                      justify=tk.LEFT, font=("Helvetica", 10), bg="#f0f0f0")

        self.command_list2 = tk.Label(right_frame, text="行のコピー: yy\n"
                                                       "貼り付け: p\n"
                                                       "直前の操作を元に戻す: u\n"
                                                       "再実行: <C-r>\n"
                                                       "テキストを置き換える: c\n"
                                                       "右にインデント: >>\n"
                                                       "左にインデント: <<\n"
                                                       "検索: /pattern\n"
                                                       "次の検索結果に移動: n\n"
                                                       "前の検索結果に移動: N\n"
                                                       "保存: :w\n"
                                                       "強制終了: :q!\n"
                                                       "保存して終了: :x\n"
                                                       "全体置換: :%s/old/new/g\n"
                                                       "終了するには q を入力してください",
                                      justify=tk.LEFT, font=("Helvetica", 10), bg="#f0f0f0")

        self.command_list1.pack(side=tk.LEFT, padx=5, pady=20, fill=tk.BOTH, expand=True)
        self.command_list2.pack(side=tk.LEFT, padx=5, pady=20, fill=tk.BOTH, expand=True)


        self.tasks = [
            "カーソルを右に移動", "カーソルを左に移動", "カーソルを上に移動", "カーソルを下に移動",
            "単語移動（次）", "単語移動（前）", "行全体削除", "複数行挿入", "現在の単語削除", "単語末尾移動",
            "行の先頭に移動", "行の末尾に移動", "テキストを挿入", "テキストを削除",
            "行のコピー", "貼り付け", "直前の操作を元に戻す", "再実行", "テキストを置き換える",
            "右にインデント", "左にインデント", "検索", "次の検索結果に移動", "前の検索結果に移動",
            "保存", "強制終了", "保存して終了", "全体置換"
        ]

        self.current_task = None

    def start_game(self, event):
        self.entry.unbind("<Return>")
        self.entry.bind("<Return>", self.check_answer)
        self.task_label.config(text="ゲームスタート！")
        self.next_task()
        self.update_timer()

    def next_task(self):
        self.current_task = random.choice(self.tasks)
        self.task_label.config(text=f"タスク: {self.current_task}")
        self.entry.delete(0, tk.END)

    def resize_text(self, event):
        new_font_size = min(max(10, event.width // 50), 20)
        new_font = ("Helvetica", new_font_size)

        self.task_label.config(font=new_font)
        self.command_list1.config(font=new_font)
        self.command_list2.config(font=new_font)
        self.score_label.config(font=new_font)
        self.timer_label.config(font=new_font)
        self.entry.config(font=new_font)


    def check_answer(self, event):
        command = self.entry.get()
        task_to_command = {
            "カーソルを右に移動": "l",
            "カーソルを左に移動": "h",
            "カーソルを上に移動": "k",
            "カーソルを下に移動": "j",
            "単語移動（次）": "w",
            "単語移動（前）": "b",
            "行全体削除": "dd",
            "複数行挿入": "o",
            "現在の単語削除": "dw",
            "単語末尾移動": "e",
            "行の先頭に移動": "0",
            "行の末尾に移動": "$",
            "テキストを挿入": "i",
            "テキストを削除": "x",
            "行のコピー": "yy",
            "貼り付け": "p",
            "直前の操作を元に戻す": "u",
            "再実行": "<C-r>",
            "テキストを置き換える": "c",
            "右にインデント": ">>",
            "左にインデント": "<<",
            "検索": "/pattern",
            "次の検索結果に移動": "n",
            "前の検索結果に移動": "N",
            "保存": ":w",
            "強制終了": ":q!",
            "保存して終了": ":x",
            "全体置換": ":%s/old/new/g"
        }

        if command == 'q':
            self.end_game()
        elif command == task_to_command.get(self.current_task):
            if self.streak == 0:
                self.score += 100
            else:
                self.score = int(self.score * 1.2)
            self.streak += 1
            self.score_label.config(text=f"スコア: {self.score}")
            self.next_task()
        else:
            self.task_label.config(text=f"不正解です。ボーナスリセット。\nタスク: {self.current_task}")
            self.score = 100  # スコアリセット
            self.streak = 0
            self.score_label.config(text=f"スコア: {self.score}")
            self.entry.delete(0, tk.END)

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=f"残り時間: {self.time_left}秒")
            self.root.after(1000, self.update_timer)
        else:
            self.end_game()

    def end_game(self):
        self.task_label.config(text=f"ゲーム終了！最終スコア: {self.score}")
        self.entry.config(state=tk.DISABLED)
        self.entry.unbind("<Return>")

        if not hasattr(self, 'button_frame'):
            self.button_frame = tk.Frame(self.root, bg="#f0f0f0")
            self.button_frame.pack(pady=10)
            self.replay_button = tk.Button(self.button_frame, text="リプレイ", command=self.replay, bg="#4CAF50", fg="white", font=("Helvetica", 12))
            self.replay_button.pack(side=tk.LEFT, padx=10)
            self.exit_button = tk.Button(self.button_frame, text="終了", command=self.root.quit, bg="#f44336", fg="white", font=("Helvetica", 12))
            self.exit_button.pack(side=tk.RIGHT, padx=10)
        else:
            self.button_frame.pack(pady=10)

    def replay(self):
        self.button_frame.pack_forget()
        self.score = 0
        self.streak = 0  # 連続数リセット
        self.time_left = 15
        self.score_label.config(text=f"スコア: {self.score}")
        self.timer_label.config(text=f"残り時間: {self.time_left}秒")
        self.entry.config(state=tk.NORMAL)
        self.entry.bind("<Return>", self.start_game)
        self.task_label.config(text="Enterキーを押してゲームを開始してください")

if __name__ == "__main__":
    root = tk.Tk()
    game = VimPracticeGame(root)
    root.mainloop()
