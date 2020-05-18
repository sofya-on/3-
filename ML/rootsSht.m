function [out1, out2] = rootsSht (p)
min = mmin(p);
max = mmax(p);
n = Shturm(p);
val = zeros(n,1);
interval = zeros(n,2);
k = 1; 
for i = max:-1:min-1
    s = Sht2(p,i-1,i);
    if s == 1
        interval(k,:)= [i-1,i];
        val(k)= dih(p,i-1,i);
        k = k + 1;
    else
        if s > 1
            i2 = i;
            for j=1:s
                [interval(k,:), val(k), i2] = cycle(p,i2);
                k = k + 1;
            end
        end
    end
end
out1 = val;
out2 = interval;
end
            
            
            