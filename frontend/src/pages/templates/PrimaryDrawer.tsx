import { Box, Typography, useMediaQuery, styled } from "@mui/material";
import { useState, useEffect } from "react";
import { useTheme } from "@mui/material/styles";
import MuiDrawer from "@mui/material/Drawer";

import DrawerToggle from "../../components/PrimaryDrawer/DrawerToggle";

const PrimaryDrawer = () => {
  const theme = useTheme();
  const isMedScreen = useMediaQuery("(max-width:599px");
  const [open, setOpen] = useState(isMedScreen);

  const openedMixin = () => ({
    transition: theme.transitions.create("width", {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.enteringScreen,
    }),
    overflowX: "hidden",
  });

  const closedMixin = () => ({
    transition: theme.transitions.create("width", {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.enteringScreen,
    }),
    overflowX: "hidden",
    width: theme.primaryDrawer.closed,
  });

  const Drawer = styled(
    MuiDrawer,
    {}
  )(({ theme, open }) => ({
    width: theme.primaryDrawer.width,
    whiteSpace: "nowrap",
    boxSizing: "border-box",
    ...(open && {
      ...openedMixin(),
      "& .MuiDrawer-paper": openedMixin(),
    }),
    ...(!open && {
      ...closedMixin(),
      "& .MuiDrawer-paper": closedMixin(),
    }),
  }));

  useEffect(() => {
    setOpen(!isMedScreen);
  }, [isMedScreen]);

  const handleDrawerClose = () => {
    setOpen(false);
  };

  const handleDrawerOpen = () => {
    setOpen(true);
  };

  return (
    <Drawer
      open={open}
      variant={isMedScreen ? "temporary" : "permanent"}
      PaperProps={{
        sx: {
          mt: `${theme.primaryAppBar.height}px`,
          height: `calc(100vh - ${theme.primaryAppBar.height}px)`,
          width: theme.primaryDrawer.width,
        },
      }}
    >
      <Box>
        <Box
          sx={{
            position: "absolute",
            top: 0,
            right: 0,
            p: 0,
            width: open ? "auto" : "100%",
          }}
        >
          <DrawerToggle
            open={open}
            handleDrawerClose={handleDrawerClose}
            handleDrawerOpen={handleDrawerOpen}
          />
          {[...Array(50)].map((_, i) => (
            <Typography key={i} paragraph>
              {i + 1}
            </Typography>
          ))}
        </Box>
      </Box>
    </Drawer>
  );
};

export default PrimaryDrawer;
