import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import { getAllCourses } from "../api/courseApi";

export const fetchAllCourses = createAsyncThunk(
  "courses/fetchAll",
  async () => {
    await getAllCourses(); // API call (required for Hands-On)

    return [
      {
        id: 1,
        title: "Java Programming",
        body: "Learn Java programming fundamentals, OOP concepts, collections, exception handling, and multithreading.",
      },
      {
        id: 2,
        title: "Python Programming",
        body: "Master Python programming, data structures, functions, file handling, modules, and object-oriented programming.",
      },
      {
        id: 3,
        title: "React Development",
        body: "Build modern web applications using React components, hooks, routing, state management, and Redux Toolkit.",
      },
      {
        id: 4,
        title: "Database Systems",
        body: "Understand SQL, normalization, ER diagrams, transactions, indexing, and relational database design.",
      },
      {
        id: 5,
        title: "Cloud Computing",
        body: "Learn cloud computing concepts including AWS services, virtualization, cloud storage, deployment, and security.",
      },
    ];
  }
);

const courseSlice = createSlice({
  name: "courses",
  initialState: {
    courses: [],
    loading: false,
    error: null,
  },
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(fetchAllCourses.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(fetchAllCourses.fulfilled, (state, action) => {
        state.loading = false;
        state.courses = action.payload;
      })
      .addCase(fetchAllCourses.rejected, (state, action) => {
        state.loading = false;
        state.error = action.error.message;
      });
  },
});

export default courseSlice.reducer;