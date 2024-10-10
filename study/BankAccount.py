import sys
import tkinter as tk
from tkinter import simpledialog, messagebox


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # 이름 맹글링을 통해 외부 접근을 더욱 어렵게 만듦

    @property
    def balance(self):
        """잔액을 확인할 때 사용하는 프로퍼티"""
        return self.__balance

    @balance.setter
    def balance(self, value):
        """잔액을 설정할 때 사용하는 프로퍼티 (값 제한 가능)"""
        if value < 0:
            raise ValueError("잔액은 0 이상이어야 합니다.")
        self.__balance = value

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            messagebox.showinfo("입금 완료", f"{amount}원이 입금되었습니다. 잔액: {self.__balance}원")
        else:
            messagebox.showerror("오류", "유효한 금액을 입금하세요.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            messagebox.showinfo("출금 완료", f"{amount}원이 출금되었습니다. 잔액: {self.__balance}원")
        else:
            messagebox.showerror("오류", "잔액이 부족하거나 유효하지 않은 금액입니다.")

    def __apply_interest(self):
        self.__balance *= 1.02  # 2% 이자 적용

    def apply_monthly_interest(self):
        self.__apply_interest()
        messagebox.showinfo("이자 적용 완료", f"이자가 적용되었습니다. 현재 잔액: {self.__balance}원")


def main():
    root = tk.Tk()
    root.withdraw()  # 기본 Tk 창 숨기기

    owner = simpledialog.askstring("계좌 소유자 입력", "계좌 소유자 이름을 입력하세요:")
    balance = simpledialog.askfloat("초기 잔액 입력", "초기 잔액을 입력하세요:")

    if owner is None or balance is None:
        messagebox.showwarning("경고", "유효한 계좌 정보를 입력해야 합니다.")
        return

    account = BankAccount(owner, balance)

    while True:
        choice = simpledialog.askstring("메뉴 선택", "1. 입금\n2. 출금\n3. 잔액 확인\n4. 이자 적용\n5. 종료\n\n원하는 작업을 선택하세요:")

        if choice == '1':
            amount = simpledialog.askfloat("입금", "입금할 금액을 입력하세요:")
            if amount is not None:
                account.deposit(amount)
        elif choice == '2':
            amount = simpledialog.askfloat("출금", "출금할 금액을 입력하세요:")
            if amount is not None:
                account.withdraw(amount)
        elif choice == '3':
            messagebox.showinfo("잔액 확인", f"현재 잔액: {account.balance}원")
        elif choice == '4':
            account.apply_monthly_interest()
        elif choice == '5':
            messagebox.showinfo("종료", "프로그램을 종료합니다.")
            break
        else:
            messagebox.showerror("오류", "잘못된 선택입니다. 다시 시도하세요.")


if __name__ == "__main__":
    main()