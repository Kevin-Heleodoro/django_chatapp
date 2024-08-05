import { createTheme } from "@mui/material";

// Adding to the existing module
declare module "@mui/material/styles" {
  // Extends the existing Theme interface
  interface Theme {
    // Add new property to Theme
    primaryAppBar: {
      height: number;
    };
  }

  // Allows us to use primaryAppBar as a global setting
  interface ThemeOptions {
    primaryAppBar?: {
      height?: number;
    };
  }
}

export const createMuiTheme = () => {
  let theme = createTheme({
    primaryAppBar: {
      height: 50,
    },
  });

  return theme;
};

export default createMuiTheme;
