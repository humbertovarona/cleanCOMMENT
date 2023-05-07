import re
import os
import sys

def remove_comments_file(content, lang):
    if lang == "c" or lang == "cpp" or lang == "java" or lang == "javascript" or lang == "objective-c":
        content = re.sub(r"\/\/.*?\n|\/\*.*?\*\/", "", content)  # C, C++, Java, Javascript, Objective-C
    elif lang == "fortran":
        content = re.sub(r"!.*?$", "", content, flags=re.MULTILINE)  # Fortran
    elif lang == lang == "R" or lang == "ruby":
        content = re.sub(r"#.*?$", "", content, flags=re.MULTILINE)  # R, Ruby
    elif lang == "matlab":
        content = re.sub(r"%.*?$", "", content, flags=re.MULTILINE)  # Matlab
    elif lang == "html":
        content = re.sub(r"<!--.*?-->", "", content, flags=re.DOTALL)  # HTML
    elif lang == "pascal":
        content = re.sub(r"\(\\\*.*?\\\*\)", "", content, flags=re.DOTALL)  # Pascal
    elif lang == "swift":
        content = re.sub(r"\/\/.*?\n", "", content)  # Swift
    elif lang == "kotlin":
        content = re.sub(r"\/\/.*?\n|\/\*.*?\*\/", "", content)  # Kotlin
    elif lang == "go":
        content = re.sub(r"\/\/.*?\n|\/\*.*?\*\/", "", content)  # Go
    elif lang == "arduino":
        content = re.sub(r"\/\/.*?\n|\/\*.*?\*\/", "", content)  # Arduino
    elif lang == "processing":
        content = re.sub(r"\/\/.*?\n|\/\*.*?\*\/", "", content)  # Processing
    elif lang == "csharp":
        content = re.sub(r"\/\/.*?\n|\/\*.*?\*\/", "", content)  # C#
    elif lang == "delphi":
        content = re.sub(r"\{\$.*?\}", "", content, flags=re.DOTALL)  # Delphi
    elif lang == "assembly":
        content = re.sub(r";.*?$", "", content, flags=re.MULTILINE)  # Assembly Language
    elif lang == "bash":
        content = re.sub(r"#.*?$", "", content, flags=re.MULTILINE)  # Bash script
    elif lang == "perl":
        content = re.sub(r"#.*?$", "", content, flags=re.MULTILINE)  # Perl
    elif lang == "SQL":
        content = re.sub(r"--.*?\n|\/\*.*?\*\/", "", content)  # SQL
    elif lang == "rust":
        content = re.sub(r"\/\/.*?\n|\/\*.*?\*\/", "", content)  # Rust
    elif lang == "scala":
        content = re.sub(r"\/\/.*?\n|\/\*.*?\*\/", "", content)  # Scala
    elif lang == "erlang":
        content = re.sub(r"%.*?$", "", content, flags=re.MULTILINE)  # Erlang
    elif lang == "haskell":
        content = re.sub(r"--.*?\n", "", content)  # Haskell
    elif lang == "lava":
        content = re.sub(r"--.*?\n", "", content)  # Lava
    elif lang == "julia":
        content = re.sub(r"#.*?$", "", content, flags=re.MULTILINE)  # Julia
    else:
        raise ValueError("Lenguaje no soportado")

    return content

def remove_empty_lines(code):
    lines = code.split("\n")
    lines = [line for line in lines if line.strip() != ""]
    return "\n".join(lines)

def read_file(filename):
    with open(filename, "rt") as f:
        content = f.read()
    return content

def save_file(filename, content):
    with open(filename, "wt") as f:
        f.write(content)

if len(sys.argv) > 1:
    code = read_file(sys.argv[1])
    clean_code = remove_comments_file(code, sys.argv[3])
    clean_code = remove_empty_lines(clean_code)
    save_file(sys.argv[2], clean_code)
    print(f"\nFile cleaned: {os.path.abspath(sys.argv[2])}\n")
else:
    print("\nType in the shell command:\n")
    print("python cleanCOMMENT.py <input_file> <output_file> <programming_language>\n")
    print("Programming languages: c, cpp, java, javascript, objective-c, fortran, R, ruby, matlab, html, pascal, "
          "haskell, swift, kotlin, arduino, processing, go, csharp, delphi, bash, perl, assembly, SQL, rust, scala, "
          "lava, julia\n")