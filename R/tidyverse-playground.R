library(nycflights13)
library(tidyverse)

ggplot(data = mpg) + 
  geom_point(mapping = aes(x = displ, y = hwy))

ggplot(data = mpg) + 
  geom_point(mapping = aes(x = displ, y = hwy, color = class))

filter(mpg, cyl > 1 & cyl < 5)

ggplot(mtcars, aes(x = wt, y = mpg)) +
  geom_point()

ggplot(mtcars, aes(x = factor(cyl))) +
  geom_bar()

# The easiest way to get forcats is to install the whole tidyverse:
install.packages("tidyverse")

# Alternatively, install just forcats:
install.packages("forcats")

library(forcats)
library(dplyr)
library(ggplot2)

starwars %>% 
  filter(!is.na(species)) %>%
  count(species, sort = TRUE)

starwars %>%
  filter(!is.na(species)) %>%
  mutate(species = fct_lump(species, n = 3)) %>%
  count(species)

ggplot(starwars, aes(x = eye_color)) + 
  geom_bar() + 
  coord_flip()

starwars %>%
  mutate(eye_color = fct_infreq(eye_color)) %>%
  ggplot(aes(x = eye_color)) + 
  geom_bar() + 
  coord_flip()

ggplot(starwars, aes(y = fct_infreq(hair_color))) + 
  geom_bar()

ggplot(starwars, aes(y = fct_infreq(fct_na_value_to_level(hair_color)))) + 
  geom_bar() + 
  labs(y = "Hair color")

starwars %>%
  count(skin_color, sort = TRUE)

starwars %>%
  mutate(skin_color = fct_lump(skin_color, n = 5)) %>%
  count(skin_color, sort = TRUE)

starwars %>%
  mutate(skin_color = fct_lump(skin_color, prop = .1)) %>%
  count(skin_color, sort = TRUE)

avg_mass_eye_color %>%
  mutate(eye_color = fct_reorder(eye_color, mean_mass)) %>%
  ggplot(aes(x = eye_color, y = mean_mass)) + 
  geom_col()
