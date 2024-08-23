import { Box } from "@mui/material";
import { useTheme } from "@mui/material/styles";

const Main = () => {
  const theme = useTheme();
  return (
    <Box
      sx={{
        flexGrow: 1,
        minWidth: `${theme.secondaryDrawer.width}px`,
        height: `calc(100vh - ${theme.primaryAppBar.height}px)`,
      }}
    >
      <p></p>
    </Box>
  );
};
