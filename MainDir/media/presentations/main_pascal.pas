begin
  var s1 := ReadString;
  var s2 := ReadString;
  var (x, y) := (s1.ToBigInteger(), s2.ToBigInteger());
  var z := x + 1;
  while (z <= y) do
  begin
    x *= z;
    z := z + 1;
  end;
  //Write(x);
  while (x div 10 > 0) do
  begin
    y := 0;
    while (x > 0) do
    begin
      y += x mod 10;
      x := x div 10;
    end;
    x := y;
  end;
  Write(x);
end.