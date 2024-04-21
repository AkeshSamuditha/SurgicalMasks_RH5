import React from "react";
import { AppBar, Toolbar, Typography, IconButton, Avatar } from "@mui/material";
// import { PowerSettingsNew } from "@mui/icons-material";
import MenuIcon from "@mui/icons-material/Menu";

function Header() {
  return (
    // <div>Header</div>
    <AppBar
      position="static"
      color="transparent"
      className="shadow-none"
      style={{ backgroundColor: "grey" }}
    >
      <Toolbar
        className="flex justify-between items-center px-4"
        style={{ paddingRight: "100px" }}
      >
        <Typography variant="h5">Prognostic</Typography>

        <Typography
          className="whitespace-nowrap mr-4"
          style={{ paddingLeft: 200, paddingRight: 890 }}
        >
          {new Date()
            .toLocaleString("en-US", {
              weekday: "long",
              month: "long",
              day: "numeric",
              year: "numeric",
              hour: "numeric",
              minute: "numeric",
              hour12: true,
            })
            .replace("at", " ")}
        </Typography>

        <Typography
          variant="body1"
          className="mr-2"
          style={{ paddingRight: 20 }}
        >
          Hi Rebecca
        </Typography>

        <Avatar />

      </Toolbar>
    </AppBar>
  );
}

export default Header;
