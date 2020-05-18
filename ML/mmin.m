function [outputArg1] = mmin(p)
p = p *sign(p(1));
q = p;

for i=1:length(p)
    if (mod(i, 2) == 0)
    	q(i) = -q(i);
    end
end

a=-1;
flag = 1;

while (flag == 1)
	a = a+1;
	sum = 0;
	flag = 0;
    for i = 1:length(p)
        sum = sum*a;
        sum = sum + q(i);
        if (sum < 0)
            flag = 1;
        end
    end
end

outputArg1 = -a;
end

