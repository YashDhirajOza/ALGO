let t = read_int ()  (* Number of test cases *)
  
let rec process_cases n =
  if n = 0 then ()
  else
    let nk = read_line () |> String.split_on_char ' ' |> List.map int_of_string in
    let n = List.nth nk 0 in
    let k = List.nth nk 1 in
    let arr = read_line () |> String.split_on_char ' ' |> List.map int_of_string in
    let rec process_array arr total_money counter =
      match arr with
      | [] -> counter  (* Base case: return the counter when array is empty *)
      | x :: xs ->
          if x = 0 then
            if total_money > 0 then
              process_array xs (total_money - 1) (counter + 1)
            else
              process_array xs total_money counter
          else if x >= k then
            process_array xs (total_money + x) counter
          else
            process_array xs total_money counter
    in
    let counter = process_array arr 0 0 in
    print_int counter;
    print_newline ();
    process_cases (n - 1)
;;

process_cases t  (* Start processing test cases *)
