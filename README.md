# MM Block Automation
This will take the images given from the `Media_gb_1.csv` on build the mm blocks, it will also populate the links of the dynamic blocks.

1. `get_products.py`
    This will fetch the products ALT via API using the SKU in the excel document provided by emerch, this will produce `mm-blocks-data-alt-output.xls` in `./resources`

2. `build.py`
    This will build the mm blocks impex found in `./production/impex`

## Before running the script

~ Install the python requirements with pip install -r requirements.txt ~

There two files that you will need before running this script.

1. `Media_gb_1.csv` - This will come from impexing the images.
2. `mm-blocks-links.xlsx` - You will need to fill these out. 
3. `mm-blocks-data.xlsx` - Deb will send you the file you may need to rename it. 

Add these both to `/resources`

## Things to note
The image namespaces will determine whether the blocks being made are `UK, US or DE` for example;
`2022-11-11_UK_US_DE_AW22_Wk25_Gifts_MM_360x258` will create blocks for all countries, however; `2022-11-11_US_DE_AW22_Wk25_Girls_MM_285x345` will only create blocks in `US & DE`.
This is why namespace is important. 

---

# How to use
1. Correctly add namespacing to the images delivered by they will often be in UK, US & DE folders, these all need to go into one. `REF: X:\WebDesign\TEMPLATE_PSDS\MM\images`
also make sure that the new in image has a capital I `_NewIn_` otherwise it the image wont be included in the html block.

2. run `get_products.py`  this will produce `mm-blocks-data-alt-output.xls` in `./resources` with the alt tags needed for the mm blocks.
3. run `build.py` this will produce the impex files 

# alternatively  
You could just run bash main in the `./components` folder this will run both of the scripts.

"# mm-block-script"  git init git add README.md git commit -m "first commit" git branch -M main git remote add origin git@github.com:turner485/mm-block-script.git git push -u origin main
"# mm-block-script" 
