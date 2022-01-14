use std::io;

fn main() {
    let mut input = String::new();
    println!("Enter a number:");
    io::stdin().read_line(&mut input).expect("Not a valid string!");

    let input: i32 = input.trim().parse().expect("No number!");

    println!("Is {} a prime? {}", input, is_prime(input))

}

fn is_prime(x: i32) -> bool {
    if x <= 1 {
        return false;
    }

    for i in 2..((x as f64).sqrt() as i32) {
        if x % i == 0 {
            return false;
        }
    }

    true
}