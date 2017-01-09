function [x,y,z] = kar_elips(fi,lam,h);
  a = 6378137.000;
  e = 0.081819191;
  fid = dms2deg(fi);
  lamd = dms2deg(lam);
  fir = (pi/180)*fid;
  lamr = (pi/180)*lamd;
  N = a/sqrt(1 - (e*2*(sin(fir)*2)));
  x = (N + h)*cos(fir)*cos(lamr);
  y = (N + h)*cos(fir)*sin(lamr);
  z = (N*(1-e*2)+ h)*sin(fir);
  
  fprintf('x = %12.9f \n', x);
  fprintf('y = %12.9f \n', y);
  fprintf('z = %12.9f \n', z);
 
end
