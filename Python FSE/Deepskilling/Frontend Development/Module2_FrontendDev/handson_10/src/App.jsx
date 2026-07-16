import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { fetchAllCourses } from "./features/courseSlice";

function App() {
  const dispatch = useDispatch();

  const { courses, loading, error } = useSelector(
    (state) => state.courses
  );

  useEffect(() => {
    dispatch(fetchAllCourses());
  }, [dispatch]);

  return (
    <div
      style={{
        padding: "20px",
        maxWidth: "1000px",
        margin: "auto",
      }}
    >
      <h1 style={{ textAlign: "center" }}>Student Portal</h1>

      {loading && <p>Loading courses...</p>}

      {error && <p style={{ color: "red" }}>Error: {error}</p>}

      {courses.map((course) => (
        <div
          key={course.id}
          style={{
            border: "1px solid gray",
            borderRadius: "8px",
            padding: "20px",
            marginBottom: "20px",
          }}
        >
          <h3>{course.title}</h3>
          <p>{course.body}</p>
        </div>
      ))}
    </div>
  );
}

export default App;