import { createTheme, responsiveFontSizes } from "@mui/material";

// Adding to the existing module
declare module "@mui/material/styles" {
  // Extends the existing Theme interface
  interface Theme {
    // Add new property to Theme
    primaryAppBar: {
      height: number;
    };
    primaryDrawer: {
      width: number;
      closed: number;
    };
  }

  // Allows us to use primaryAppBar as a global setting
  interface ThemeOptions {
    primaryAppBar?: {
      height?: number;
    };
    primaryDrawer: {
      width?: number;
      closed?: number;
    };
  }
}

export const createMuiTheme = () => {
  let theme = createTheme({
    typography: {
      fontFamily: ["IBM Plex Sans", "sans-serif"].join(","),
    },
    primaryAppBar: {
      height: 50,
    },
    primaryDrawer: {
      width: 240,
      closed: 70,
    },
    components: {
      MuiAppBar: {
        styleOverrides: {
          root: {
            boxShadow: "none",
            color: "#000",
          },
        },
      },
    },
  });

  theme = responsiveFontSizes(theme);

  return theme;
};

export default createMuiTheme;
