from linguist.libs.file_blob import FileBlob

FileBlob('test.py').language.name #=> 'Python'

#read url text instead of text files
##import urllib
##
##link = "https://stackoverflow.com/questions/15138614/how-can-i-read-the-contents-of-an-url-with-python"
##f = urllib.urlopen(link)
##myfile = f.read()
##print myfile


#variables
inPath = r'C:\Users\b020719\Desktop\test1.txt' #wgs84 EPSG:4326
outPath = r'C:\Users\b020719\Desktop\test2.txt' #wgs84 EPSG:4326

#read file
try:
 infile = open(inPath, "r")
 data = infile.read().replace('\n', '')#replaces newline caracters if they exist
 infile.close()
 print "\nData read from " + inPath + "\n"
except Exception:
 pass
 print "\nFailed to get data from " + inPath + "\n"

#4test string = ((((13.9063613534021,56.6241836957076),(13.9062936907774,56.624232391028),(13.9062182104013,56.6242752494389),(13.9061743018877,56.6243383492587),(13.9061705498975,56.6244128441878),(13.9061696595372,56.6244954684476),(13.9061296430574,56.6245783957052),(13.9060920652447,56.6246451899343),(13.9060450407738,56.6247055489462),(13.9059313888165,56.6247945403959),(13.9058015456844,56.6248814756514),(13.9056743355337,56.624981039429),(13.9055482564132,56.6250904961707),(13.9054334217794,56.6252028099799),(13.9053436225993,56.6253038435074),(13.9053376945838,56.6253087419229),(13.9060204582497,56.6255147444791),(13.9065618974825,56.6254219830821),(13.9075918305922,56.6252476596177),(13.9079907337967,56.6253860473895),(13.9081175830759,56.6255539698383),(13.9086065435267,56.6261086419057),(13.9089424537032,56.6265642170437),(13.9092657225354,56.6268745869601),(13.9096073170035,56.6269786667958),(13.9102496630114,56.6271268976407),(13.9108716919925,56.6273627006044),(13.9113195000399,56.6274947579675),(13.9119175056545,56.6276532839925),(13.9123795042684,56.6277416253763),(13.9137056414057,56.6279714808347),(13.9139071154617,56.6280372459431),(13.9140985147736,56.6281530213031),(13.9142387890716,56.6283809012355),(13.9144244287709,56.6289602523823),(13.9145979544147,56.6291429594941),(13.9194378896811,56.6242789919882),(13.9191095750058,56.6241527185745),(13.9100762413899,56.627007787649),(13.9083726039218,56.6242400060313),(13.9081681797173,56.6238963907132),(13.9074397668897,56.6236198107434),(13.9074181399505,56.6237506534149),(13.9074062410419,56.6238025882024),(13.9073816912019,56.6240052556689),(13.9073950768545,56.6241562888137),(13.9073874187854,56.6242639568425),(13.9063613534021,56.6241836957076))))

#replace stuff in string from inPath
a = str(data).replace("),(", "//")
b = str(a).replace(",", " ")
c = "MULTIPOLYGON " + str(b).replace("//", ", ")
d = str(c).replace(r"((((", "(((")
e = str(d).replace(r"))))", ")))")

print e

#write file
try:
 text_file = open(outPath, "w")
 text_file.write(e)
 text_file.close()
 print "\nSuccess, string written to " + outPath
except Exception:
 pass
 print "\nFailed to write file " + outPath
