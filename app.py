from PIL import Image
import os

def resize_images(input_dir, output_dir, size=(300, 300)):

    # Redimensiona todas as imagens de um diretório para o tamanho especificado.

    # Args:
    #     input_dir (str): Caminho para o diretório com as imagens originais.
    #     output_dir (str): Caminho para o diretório onde as imagens redimensionadas serão salvas.
    #     size: Tamanho desejado das imagens (largura, altura).

    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    if not os.path.exists(input_dir):
        os.makedirs(input_dir)

    
    for filename in os.listdir(input_dir):
        input_path = os.path.join(input_dir, filename)
   
        if os.path.isfile(input_path) and filename.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif')):
            try:
                
                with Image.open(input_path) as img:
                    
                    img_resized = img.resize(size, Image.Resampling.LANCZOS)

                    output_path = os.path.join(output_dir, filename)

                    img_resized.save(output_path)
                    
                    print(f"Imagem {filename} redimensionada e salva em {output_path}")
            except Exception as e:
                print(f"Erro ao processar {filename}: {e}")


input_directory = "./input"  # Substitua pelo caminho do seu diretório de entrada
output_directory = "./output"  # Substitua pelo caminho do seu diretório de saída


resize_images(input_directory, output_directory)
