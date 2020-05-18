function [der] = derivative(p)
if (length(p) ~= 1) 
    newp = p;
    newp(end)= [];
    for i=1:length(newp)
        newp(i) = newp(i)*abs(length(newp)-i+1);
    end
    der = newp;
else
    der = 0;
end