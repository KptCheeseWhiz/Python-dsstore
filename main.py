import dsstore
import os
import sys

def main():
    for file in sys.argv[1:]:
      if not os.path.exists(file):
        continue
      with open(file, "rb") as f:
          print(">", file)
          d = dsstore.DS_Store(f.read(), debug=False)
          files = d.traverse_root()
          for f in files:
              print(">>", f)

if __name__ == "__main__":
    main()