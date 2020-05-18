function [out1, out2, out3] = cycle(p,i)
z = 1;
while Sht2(p,i-z,i) ~= 1
    z = z/2;
end
out1 = [i-z,i];
out2 = dih(p,i-z,i);
out3 = i-z;
end