numri = int(input("Shkruaj një numër: "))  # Merr inputin
numri_origjinal = numri  # Ruajmë numrin origjinal për printim
numri_mbrapsht = 0

while numri > 0:
    shifra = numri % 10  # Merr shifrën e fundit
    numri_mbrapsht = numri_mbrapsht * 10 + shifra  # Shton shifrën në numrin e ri
    numri //= 10  # Heq shifrën e fundit

print(f"Numri {numri_origjinal} i kthyer mbrapsht është {numri_mbrapsht}")

