function [out] = Sht2 (p,a,b)
d = cell(1, length(p));
d{1,1} = p;
d{1,2} = derivative(p);
p3 = p;
i = 3;
while length(p3)>1
    [p2,p3] = division(d{1,i-2}, d{1,i-1});
    d{1,i} = p3*(-1);
    i = i+1;
end
zn1 = 0;
zn2 = 0;
for i = 1:length(d)-1
    if sign(gorner(d{1,i},a))~=sign(gorner(d{1,i+1},a))
        zn1 = zn1 + 1;
    end
    if sign(gorner(d{1,i},b))~=sign(gorner(d{1,i+1},b))
        zn2 = zn2 + 1;
    end
end
out = zn1-zn2;
end