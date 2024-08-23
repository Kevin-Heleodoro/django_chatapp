import { Box, CssBaseline } from "@mui/material";

import PrimaryAppBar from "./templates/PrimaryAppBar";
import PrimaryDrawer from "./templates/PrimaryDrawer";
import SecondaryDrawer from "./templates/SecondaryDrawer";

const Home = () => {
  return (
    <Box
      sx={{
        display: "flex",
      }}
    >
      <CssBaseline />
      <PrimaryAppBar />
      <PrimaryDrawer></PrimaryDrawer>
      <SecondaryDrawer></SecondaryDrawer>
    </Box>
  );
};

export default Home;
