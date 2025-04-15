import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
import pyperclip

class GeradorSenha:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Gerador de Senhas Seguras")
        self.window.geometry("500x400")
        self.window.resizable(False, False)
        
        # Configuração do estilo
        self.style = ttk.Style()
        self.style.configure('TButton', font=('Arial', 12))
        self.style.configure('TLabel', font=('Arial', 12))
        
        self.setup_ui()
        
    def setup_ui(self):
        # Frame principal
        main_frame = ttk.Frame(self.window, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        titulo = ttk.Label(main_frame, text="Gerador de Senhas Seguras", font=('Arial', 16, 'bold'))
        titulo.pack(pady=10)
        
        # Frame para entrada
        input_frame = ttk.Frame(main_frame)
        input_frame.pack(fill=tk.X, pady=10)
        
        # Label e entrada para tamanho
        ttk.Label(input_frame, text="Tamanho da senha:").pack(side=tk.LEFT, padx=5)
        self.tamanho_var = tk.StringVar()
        self.tamanho_entry = ttk.Entry(input_frame, textvariable=self.tamanho_var, width=5)
        self.tamanho_entry.pack(side=tk.LEFT, padx=5)
        
        # Checkboxes para opções
        options_frame = ttk.Frame(main_frame)
        options_frame.pack(fill=tk.X, pady=10)
        
        self.letras_var = tk.BooleanVar(value=True)
        self.numeros_var = tk.BooleanVar(value=True)
        self.especiais_var = tk.BooleanVar(value=True)
        
        ttk.Checkbutton(options_frame, text="Letras", variable=self.letras_var).pack(side=tk.LEFT, padx=5)
        ttk.Checkbutton(options_frame, text="Números", variable=self.numeros_var).pack(side=tk.LEFT, padx=5)
        ttk.Checkbutton(options_frame, text="Caracteres especiais", variable=self.especiais_var).pack(side=tk.LEFT, padx=5)
        
        # Botão gerar
        ttk.Button(main_frame, text="Gerar Senha", command=self.gerar_senha).pack(pady=10)
        
        # Área de resultado
        result_frame = ttk.Frame(main_frame)
        result_frame.pack(fill=tk.X, pady=10)
        
        self.senha_var = tk.StringVar()
        self.senha_entry = ttk.Entry(result_frame, textvariable=self.senha_var, state='readonly', font=('Arial', 12))
        self.senha_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        
        ttk.Button(result_frame, text="Copiar", command=self.copiar_senha).pack(side=tk.RIGHT, padx=5)
        
    def gerar_senha(self):
        try:
            tamanho = int(self.tamanho_var.get())
            if tamanho <= 0 or tamanho > 100:
                raise ValueError("O tamanho deve estar entre 1 e 100")
            
            caracteres = ""
            if self.letras_var.get():
                caracteres += string.ascii_letters
            if self.numeros_var.get():
                caracteres += string.digits
            if self.especiais_var.get():
                caracteres += string.punctuation
                
            if not caracteres:
                raise ValueError("Selecione pelo menos um tipo de caractere")
                
            senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
            self.senha_var.set(senha)
            
        except ValueError as e:
            messagebox.showerror("Erro", str(e))
        except Exception as e:
            messagebox.showerror("Erro", "Ocorreu um erro ao gerar a senha")
            
    def copiar_senha(self):
        senha = self.senha_var.get()
        if senha:
            pyperclip.copy(senha)
            messagebox.showinfo("Sucesso", "Senha copiada para a área de transferência!")
            
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = GeradorSenha()
    app.run()


