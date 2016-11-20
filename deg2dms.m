function dms=deg2dms(deg)

if (deg < 0)
	kot=-deg;
else 
	kot=deg;
end

st=floor(kot);
min=floor((kot-st)*60.);
sek=((kot-st)*60.-min)*60.;

if abs(sek-60.0)<1e-10
    sek=0;
    min=min+1;
end

if min==60;
    min=0;
    st=st+1;
end

if abs(sek-100)<0.001
    sek  = 0;
    min = min +1;
end

if min == 60;
    min = 0;
    st = st+1;
end

dms=st+min/100.+sek/10000.;

if (deg<0)
	dms=-dms;
end