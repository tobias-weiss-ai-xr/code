fn main() {
    println!("Hello, world!");

    another_fn(5, 'm');

    println!("Five: {}", five());

    let _x = plus_one(five());
}

fn another_fn(x: i32, unit_label: char) {
    let x = {
        let y = x;
        y + 3
    };
    println!("x value: {} {}", x, unit_label);
}

fn five() -> i32 {
    5
}

fn plus_one(x: i32) -> i32 {
    x + 1
}