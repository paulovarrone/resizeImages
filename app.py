from PIL import Image, ImageOps
import os

<<<<<<< HEAD
def resize_images(input_dir, output_dir, size=(300, 400)):
    # Cria os diretórios se não existirem
=======
def resize_images(input_dir, output_dir, size=(300, 300)):

    # Redimensiona todas as imagens de um diretório para o tamanho especificado.

    # Args:
    #     input_dir (str): Caminho para o diretório com as imagens originais.
    #     output_dir (str): Caminho para o diretório onde as imagens redimensionadas serão salvas.
    #     size: Tamanho desejado das imagens (largura, altura).

    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
>>>>>>> e249a6d7cc624a21412d681a511c368e5e58ac24
    if not os.path.exists(input_dir):
        os.makedirs(input_dir)
        print(f"Pasta de entrada criada: {input_dir}")
        print("Coloque as imagens que deseja redimensionar dentro desta pasta e execute o script novamente.")
        return

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Pasta de saída criada: {output_dir}")

    imagens = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f)) and f.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif'))]

    if not imagens:
        print(f"Nenhuma imagem encontrada na pasta: {input_dir}")
        print("Coloque imagens na pasta de entrada e execute novamente.")
        return

    # Processa cada imagem
    for filename in imagens:
        input_path = os.path.join(input_dir, filename)

        try:
            with Image.open(input_path) as img:
                img = ImageOps.exif_transpose(img)
                img_resized = img.resize(size, Image.Resampling.LANCZOS)

                output_path = os.path.join(output_dir, filename)
                img_resized.save(output_path)

                print(f"Imagem {filename} redimensionada e salva em {output_path}")
        except Exception as e:
            print(f"Erro ao processar {filename}: {e}")

# Define os diretórios
input_directory = "./input"
output_directory = "./output"

# Executa a função
resize_images(input_directory, output_directory)
