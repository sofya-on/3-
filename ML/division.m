function [outputArg1,outputArg2] = division (p1, p2)
newp = zeros(length(p2), length(p1));
newp(1,:) = p1;
[m,n] = size(newp);
d = p2(1);
p2(1) = [];
p2 = p2*(-1);
ost = zeros(1, length(p2));
res = zeros(1,length(p1) - length(p2));
for i=1:length(res)
    res(i) = sum(newp(:,i)) / d;
    for k=1:length(p2)
        newp(m-k+1,i+k) = res(i)*p2(k);
    end
end
for i=(length(res)+1):length(p1)
    ost(i-length(res)) = sum(newp(:,i));
end
outputArg1 = res;
outputArg2 = ost;
end

