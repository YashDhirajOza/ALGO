let read_int () = Scanf.scanf " %d" (fun x -> x)
let sum_of_digits n =
  let tens = n / 10 in
  let units = n mod 10 in
  tens + units
let () =
  let t = read_int () in
  for _ = 1 to t do
    let n = read_int () in
    Printf.printf "%d\n" (sum_of_digits n)
  done
