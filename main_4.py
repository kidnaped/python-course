#slicing = create a substring by extracting elements from another string
#           indexting[] or slice()
#           [start:stop:step]
#           start is including number, stop - excluding (so we add 1 to it)

#name = "Chyort Sobachiy"
#first_name = name[0:6]                              #[:6]
#sec_name = name[(len(first_name)+1):(len(name)+1)]  #[15:]
#funky_name = name[0:(len(name)+1):2]                #[::2]
#reversed_name = name[::-2]                          #[0:end:-1]

#print(first_name)
#print(sec_name)
#print(funky_name.upper())
#print(reversed_name)

website = "https://shmurdyak.uk"
slice = slice((website.find("/")+2),(website.find(".")-len(website)))
# or you can manually calculate nubers of symbols, like slice(7,-4)
print(website[slice].capitalize())
