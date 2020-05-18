function [out] = dih(p,b,a)
  eps=0.000001;
  x = 0;
  while abs(b - a) >= eps
      x = (a + b) / 2;
      if sign(gorner(p, a)) == sign(gorner(p, x))
          a = x;
      else
          b = x;
      end
  end
  [out] = x;
end
