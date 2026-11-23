import sys
import pypdf

def main():
    dest = pypdf.PdfWriter()

    pdf_name = sys.argv[1];
    source = pypdf.PdfReader(pdf_name)
    pages = len(source.pages)
    if pages % 2 == 1 :
        pages += 1

    right_side = 0
    left_side = int(pages / 2)
    for i in range(pages) :
        try :
            if i % 2 == 0 :
                dest.append(source, (right_side, right_side+1));
                right_side += 1
            else :
                dest.append(source, (left_side, left_side+1));
                left_side += 1
        except :
            break

    dest_name = pdf_name.split(".")[0] + "_A5.pdf";
    dest.write(dest_name)

if __name__ == "__main__":
    main()
