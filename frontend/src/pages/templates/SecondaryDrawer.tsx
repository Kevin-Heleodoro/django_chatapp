import { Box, Typography } from "@mui/material";
import { useTheme } from "@mui/material/styles";
import axios from "axios";

const SecondaryDrawer = () => {
  const theme = useTheme();

  const URL = "http://127.0.0.1:8000/api/server/select/?category=Wellness";
  axios
    .get(URL)
    .then((res) => {
      console.log(res.data);
    })
    .catch((err) => {
      console.error(err);
    });

  return (
    <Box
      sx={{
        minWidth: `${theme.secondaryDrawer.width}px`,
        height: `calc(100vh - ${theme.primaryAppBar.height}px)`,
        mt: `${theme.primaryAppBar.height}px`,
        borderRight: `1px solid ${theme.palette.divider}`,
        display: { xs: "none", sm: "block" },
        overflow: "auto",
      }}
    >
      {[...Array(50)].map((_, i) => (
        <Typography key={i} paragraph>
          {i + 1}
        </Typography>
      ))}
    </Box>
  );
};

export default SecondaryDrawer;
