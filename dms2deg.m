function deg=dms2deg(dms)

if (dms < 0)
	kot=abs(dms);
else 
	kot=dms;
end

st=floor(kot);
min=floor((kot-st)*100.);
sek=((kot-st)*100. - min)*100.;

if abs(sek - 100) < 1e-5
    sek = 0;
    min = min + 1;
end


deg=st+min/60.+sek/3600.;

if (dms<0)
	deg=-deg;
end