// run rustc main.rs && ./main
fn main(){
    println!("Hello, world!");
    let mut s = String::from("hello");
    s.push_str(", world!"); // append literal to string
    println!("{}", s);
}
