import tkinter as tk

from get_info import get_band_lists, get_post_key
from get_new_post_key import checking_new_post, get_new_post_key


class SimpleApp:
    def __init__(self, master):
        self.token = None
        self.band_key = None
        self.post_key = None
        self.message = None

        self.master = master
        master.title("승마 클럽 메크로")

        # 1. Access Token 입력란 ----------------------------------------------
        self.label_1 = tk.Label(master, text="\n네이버 밴드에서 받은 Access Token을 넣어주세요.")
        self.label_1.grid(row=0, column=0, sticky="w")

        self.entry_1 = tk.Entry(master, width=30) 
        self.entry_1.grid(row=1, column=0, sticky="w")

        self.button_1 = tk.Button(master, text="Confirm", command=self.confirm_1)
        self.button_1.grid(row=1, column=1, sticky="e")  # 오른쪽 끝에 붙이기

        # 1.1 Access Token 이 잘 작동한다면 가입된 밴드의 이름과 Band_key가 출력되는 부분 -------
        self.output_text_1 = tk.Text(master, height=4, width=50)
        self.output_text_1.grid(row=2, column=0, columnspan=2, sticky="w") 

        # 2. band_key 입력란 ----------------------------------------------
        self.label_2 = tk.Label(master, text="\n내가 원하는 밴드의 이름 뒤에 있는 영어를 복사해주세요.")
        self.label_2.grid(row=6, column=0, sticky="w")

        self.entry_2 = tk.Entry(master, width=30) 
        self.entry_2.grid(row=7, column=0, sticky="w")

        self.button_2 = tk.Button(master, text="Confirm", command=self.confirm_2)
        self.button_2.grid(row=7, column=1, sticky="e")  

        # 3. 원하는 텍스트 입력 -----------------------------------------------
        self.label_3 = tk.Label(master, text="\n원하는 댓글을 적어주세요.")
        self.label_3.grid(row=8, column=0, sticky="w")

        self.entry_3 = tk.Text(master, height=3, width=40) 
        self.entry_3.grid(row=9, column=0, sticky="w")

        self.button_3 = tk.Button(master, text="Confirm", command=self.confirm_3)
        self.button_3.grid(row=9, column=1, sticky="e")  # 오른쪽 끝에 붙이기

        # 4. 메크로 시작 ----------------------------------------------------
        self.start_button = tk.Button(master, text="메크로 시작", command=self.start)
        self.start_button.grid(row=12, column=0, columnspan=2, pady=10)  


    def confirm_1(self):
        self.token = self.entry_1.get()
        band_values = get_band_lists(self.token)
        
        output_text_1 = ""
        for band in band_values:
            for name, key in band.items():
                output_text_1 += f"{name:<9} {key}\n" 
        self.output_text_1.delete(1.0, tk.END)
        self.output_text_1.insert(tk.END, output_text_1) 
        print("------ 1. access token is checked ------")
        print(f"access token: {self.token}\n")

    def confirm_2(self):
        self.band_key = self.entry_2.get()
        print("------ 2. band_key is checked ------")
        print(f"band_key: {self.band_key}\n")

    def confirm_3(self):
        self.message = self.entry_3.get("1.0", tk.END)
        print("------ 3. my message is checked ------")
        print(f'{self.entry_3.get("1.0", tk.END)}\n')

    def start(self):
        print("Start button clicked.")
        checking_new_post(self.token, self.band_key, self.message)

        # 여기에 시작 버튼을 클릭했을 때 실행할 동작을 추가하세요.


        
if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleApp(root)
    root.geometry("400x400")
    root.mainloop()
