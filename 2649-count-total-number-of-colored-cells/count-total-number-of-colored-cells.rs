impl Solution {
    pub fn colored_cells(n: i32) -> i64 {
        1 + 2 * (n - 1) as i64 * n as i64
    }
}
