fn main() {
    let mut number = 3;
    while number > 0 {
        println!("{}!", number);
        number -= 1;
    }
    println!("Liftoff!");

    // another example
    let a = [10, 20, 30, 40, 42];
    let mut index = 0;

    while index < 5 {
        println!("the value ist : {}", a[index]);
        index += 1;
    }

    // another example
    for element in a {
        println!("the value ist : {}", element);
    }

    for number in (1..4).rev() {
        println!("{}!", number);
    }
    println!("LIFTOFF!!!");
}
