import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import ImageTk
import os

from download import Download
from imagem import Imagem
from Filtros import PretoBranco, EscalaCinza, Contorno, Cartoon, Negativo, Blurred


class AppImagem:

    def __init__(self, root):
        self.root = root
        self.root.title("Aplicação de Filtros em Imagem")
        self.root.geometry("900x500")
        self.caminho_imagem = None
        self.imagem_original = None
        self.imagem_filtrada = None
        self.tk_imagem = None

        self.filtros = {
            "Preto e Branco": PretoBranco.aplicar_pb,
            "Escala de Cinza": EscalaCinza.aplicar_cinza,
            "Contorno": Contorno.aplicar_contorno,
            "Cartoon": Cartoon.aplicar_cartoon,
            "Negativo": Negativo.aplicar_negativo,
            "Borrado (Blur)": None  # blur recebe intensidade
        }

        # =======================================
        # 1. MENU ESQUERDO
        # =======================================
        self.menu = tk.LabelFrame(root, text="Menu Principal", padx=10, pady=10)
        self.menu.pack(side="left", fill="y")

        tk.Label(self.menu, text="Caminho / URL da imagem:").pack()
        self.entry_caminho = tk.Entry(self.menu, width=40)
        self.entry_caminho.pack(pady=5)

        tk.Button(self.menu, text="Selecionar arquivo", command=self.selecionar_arquivo)\
            .pack(fill="x", pady=3)

        tk.Button(self.menu, text="Carregar imagem", command=self.carregar_imagem)\
            .pack(fill="x", pady=3)

        # --- Lista de filtros ---
        tk.Label(self.menu, text="Escolha o filtro:").pack(pady=5)
        self.listbox = tk.Listbox(self.menu, height=7)
        for filtro in self.filtros.keys():
            self.listbox.insert(tk.END, filtro)
        self.listbox.pack(pady=5)

        tk.Label(self.menu, text="Intensidade Blur (1-10):").pack()
        self.blur_scale = tk.Scale(self.menu, from_=1, to=10, orient="horizontal")
        self.blur_scale.pack()

        tk.Button(self.menu, text="Aplicar filtro", command=self.aplicar_filtro)\
            .pack(fill="x", pady=10)

        tk.Button(self.menu, text="Listar imagens do diretório", command=self.listar_imagens)\
            .pack(fill="x", pady=3)

        tk.Button(self.menu, text="Sair", command=self.root.quit)\
            .pack(fill="x", pady=3)

        # =======================================
        # 2. ÁREA DE VISUALIZAÇÃO
        # =======================================
        self.visual = tk.LabelFrame(root, text="Visualização", padx=10, pady=10)
        self.visual.pack(side="right", fill="both", expand=True)

        self.canvas = tk.Canvas(self.visual, bg="white")
        self.canvas.pack(fill="both", expand=True)

        # texto de metadados
        self.info_text = tk.Text(self.visual, height=8)
        self.info_text.pack(fill="x")

    # =====================================================
    # FUNÇÕES DO MENU
    # =====================================================

    def selecionar_arquivo(self):
        caminho = filedialog.askopenfilename(
            filetypes=[("Imagens", "*.jpg *.png"), ("Todos os Arquivos", "*.*")]
        )
        if caminho:
            self.entry_caminho.delete(0, tk.END)
            self.entry_caminho.insert(0, caminho)

    # --------------------------------------------------

    def carregar_imagem(self):
        caminho = self.entry_caminho.get().strip()

        # Caso seja URL: baixa a imagem
        if caminho.startswith("http://") or caminho.startswith("https://"):
            nome = "download_temp.png"
            baixador = Download(caminho, nome)
            baixador.baixarArquivo()
            caminho = nome

        # Verifica arquivo local
        if not os.path.isfile(caminho):
            messagebox.showerror("Erro", "Arquivo não encontrado.")
            return

        try:
            self.imagem_original = Imagem(1, "imagem", caminho).conteudo()
            self.caminho_imagem = caminho
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao abrir imagem.\n{e}")
            return

        self.mostrar_imagem(self.imagem_original)
        self.exibir_info()

    # --------------------------------------------------

    def mostrar_imagem(self, img):
        """Exibe a imagem no Canvas."""
        largura = self.canvas.winfo_width()
        altura = self.canvas.winfo_height()

        img_resized = img.copy()
        img_resized.thumbnail((largura, altura))

        self.tk_imagem = ImageTk.PhotoImage(img_resized)
        self.canvas.delete("all")
        self.canvas.create_image(largura // 2, altura // 2, image=self.tk_imagem)

    # --------------------------------------------------

    def aplicar_filtro(self):
        if self.imagem_original is None:
            messagebox.showwarning("Aviso", "Nenhuma imagem carregada.")
            return

        selecao = self.listbox.curselection()
        if not selecao:
            messagebox.showwarning("Aviso", "Selecione um filtro.")
            return

        nome_filtro = self.listbox.get(selecao[0])

        # Blur tem tratamento especial
        if nome_filtro == "Borrado (Blur)":
            intensidade = self.blur_scale.get()
            self.imagem_filtrada = Blurred.aplicar_blurred(self.imagem_original, intensidade)
        else:
            self.imagem_filtrada = self.filtros[nome_filtro](self.imagem_original)

        self.mostrar_imagem(self.imagem_filtrada)

        # SALVAR AUTOMATICAMENTE
        self.imagem_filtrada.save("resultado.png")
        messagebox.showinfo("Sucesso", "Filtro aplicado.\nArquivo salvo como: resultado.png")

    # --------------------------------------------------

    def listar_imagens(self):
        arquivos = [a for a in os.listdir(".") if a.lower().endswith((".jpg", ".png"))]

        self.info_text.delete("1.0", tk.END)
        if arquivos:
            for arq in arquivos:
                self.info_text.insert(tk.END, f"- {arq}\n")
        else:
            self.info_text.insert(tk.END, "Nenhuma imagem encontrada.\n")

    # --------------------------------------------------

    def exibir_info(self):
        img = Imagem(1, "imagem", self.caminho_imagem)

        self.info_text.delete("1.0", tk.END)
        self.info_text.insert(tk.END, str(img))

if __name__ == "__main__":
    root = tk.Tk()
    app = AppImagem(root)
    root.mainloop()
