import subprocess
import sys

import pypdf


# A reorganização asume que você ira imprimir o PDF em formato A5,
# frente e verso, com 4 paginas por folha.
# A primeira metade do arquivo ficara do lado esquerdo das folhas
# impressas, e a segunda metade do lado direito, basta cortar no meio
# e jogar todas as folhas do lado direito para o fundo.
def main():
    if len(sys.argv) != 2 :
        print("Pase apenas o nome do PDF que deseja reordenar.")
        return

    pdf_name = sys.argv[1];
    try :
        # Verifica se o arquivo passado é um PDF valido
        result = subprocess.run(["file", pdf_name], capture_output=True, text=True, check=True)
        if result.stderr != '' :
            print(result.stderr)
            return

        if len(result.stdout.split("PDF document")) != 2 :
            print("Arquivo não é um PDF valido.")
            return

    except FileNotFoundError :
        print("Falha ao tentar identificar o arquivo.")
        return

    dest = pypdf.PdfWriter()
    source = pypdf.PdfReader(pdf_name)
    pages = len(source.pages)
    if pages % 2 == 1 :
        pages += 1

    right_side = 0
    left_side = int(pages / 2)
    for i in range(pages) :
        try :
            # Pagians do lado esquerdo da folha, 1º metade
            if i % 2 == 0 :
                dest.append(source, (right_side, right_side+1));
                right_side += 1

            # Pagians do lado direito da folha, 2º metade
            else :
                dest.append(source, (left_side, left_side+1));
                left_side += 1

        # arquivo chegou no no final, e possui quantidade impar de paginas
        except IndexError:
            break

    # Exporta o novo PDF reordenado
    dest_name = pdf_name.split(".")[0] + "_A5.pdf";
    dest.write(dest_name)
    print("PDF exportado com sucesso:", dest_name)

if __name__ == "__main__":
    main()
