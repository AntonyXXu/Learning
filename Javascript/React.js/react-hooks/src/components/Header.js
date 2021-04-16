//optional
import React from "react";
import Button from "./Button";

import PropTypes from "prop-types";

const Header = ({ title, onAddButton, showAdd }) => {
  return (
    <header className="header">
      <h1>{title}</h1>
      <Button
        color={showAdd ? "red" : "green"}
        text={showAdd ? "Close Add Button" : "Show Add Button"}
        onClick={onAddButton}
      />
    </header>
  );
};

Header.defaultProps = {
  title: "task tracker",
};

Header.propTypes = {
  title: PropTypes.string,
};

export default Header;
