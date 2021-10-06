név = input('add meg a gép tipusát?')
Működik = True if input('Működik (i/n)?') == 'i' else False 
ár = int(input('MI az ára?'))
if (név == 'ZX Spectrum' or név == 'c64') and Működik and ár <= 25000:
    print('gg ez!')

else:
    print('nincs biznisz!')

