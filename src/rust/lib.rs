use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

#[pyfunction]
fn testing() {
    println!("hello from rust via pyo3");
}

#[pymodule]
fn rustmoda(_py: Python<'_>, m: &PyModule) -> PyResult<()> {
    m.add_wrapped(wrap_pyfunction!(testing))?;

    Ok(())
}
