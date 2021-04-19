import React, { Component } from "react";
import Header from "./Components/layout/Header";
import Todos from "./Components/Todos";
import AddToDo from "./Components/AddToDo";
import { v4 as uuid } from "uuid";
import { BrowserRouter as Router, Route } from "react-router-dom";
import About from "./pages/about";
import "./App.css";

class App extends Component {
  state = {
    todoList: [
      {
        id: uuid(),
        title: "task1",
        completed: false,
      },
      {
        id: uuid(),
        title: "task2",
        completed: false,
      },
      {
        id: uuid(),
        title: "task3",
        completed: false,
      },
    ],
  };
  markComplete = (id) => {
    this.setState({
      todoList: this.state.todoList.map((todo) => {
        if (todo.id === id) {
          todo.completed = !todo.completed;
        }
        return todo;
      }),
    });
  };

  delTodo = (id) => {
    this.setState({
      todoList: [...this.state.todoList.filter((todo) => todo.id !== id)],
    });
  };

  addToDo1 = (title) => {
    const newTodo = {
      id: uuid(),
      title: title,
      completed: false,
    };
    this.setState({ todoList: [...this.state.todoList, newTodo] });
  };

  render() {
    return (
      <Router>
        <div className="App">
          <div className="Container">
            <Header />
            <Route
              exact
              path="/"
              render={(props) => (
                <React.Fragment>
                  <AddToDo addToDo1={this.addToDo1} />
                  <Todos
                    todoList={this.state.todoList}
                    markComplete={this.markComplete.bind(
                      this.props.markComplete
                    )}
                    delTodo={this.delTodo}
                  />
                </React.Fragment>
              )}
            />
            <Route path="/about" component={About} />
          </div>
        </div>
      </Router>
    );
  }
}
export default App;
