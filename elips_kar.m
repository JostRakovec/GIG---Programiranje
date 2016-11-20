function [fi,lam,h] = elips_kar(x,y,z); 
  a = 6378137.000;
  e = 0.081819191;
  p = sqrt(x^2 + y^2);
  b = a * sqrt(1 - e^2);
  e20 = sqrt(e^2 / (1 - e^2));
  o = atan((z * a)/(p * b));
  fi= atan((z + e20^2 * b * sin(o)^3)/(p- e^2 * a * cos(o)^3));
  lam = atan(y/x);
  N = a / (sqrt(1 - e^2 * sin(fi)^2));
  h= (p/cos(fi))- N;
  fid = fi*180/pi;
  lamd = lam*180/pi;
  fiDMS = deg2dms(fid);
  lamDMS = deg2dms (lamd);
  
  fprintf('fi = %12.9f \n', fiDMS)
  fprintf('lam = %12.9f \n', lamDMS)
  fprintf('h = %12.4f \n', h)
endfunction
