import React, { Component } from "react";

export class AddToDo extends Component {
  state = {
    title: "",
  };
  onChangeMtd = (e) => this.setState({ title: e.target.value });
  onSubmitMtd = (e) => {
    e.preventDefault();
    this.props.addToDo1(this.state.title);
    //this.setState({ title: "" });
  };
  render() {
    return (
      <form onSubmit={this.onSubmitMtd} style={{ display: "flex" }}>
        <input
          type="text"
          name="title"
          placeholder="add to"
          style={{ flex: "1", padding: "5px" }}
          value={this.state.title}
          onChange={this.onChangeMtd}
        />

        <input
          type="submit"
          value="submit"
          className="btn"
          style={{ flex: "1" }}
        />
      </form>
    );
  }
}
export default AddToDo;
