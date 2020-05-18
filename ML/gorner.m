function [outputArg1] = gorner(p, a)
sum =0;
for i=1:length(p)
    sum = sum *a;
    sum = sum + p(i);
end
outputArg1 = sum;
end