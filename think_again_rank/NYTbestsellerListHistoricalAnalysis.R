## Data taken from https://www.kaggle.com/dhruvildave/new-york-times-best-sellers

rawData <- read.csv("bestsellers2.csv", stringsAsFactors = FALSE)
data <- rawData[rawData$list_name == "Combined Print and E-Book Nonfiction",]
weeks <- unique(data$published_date)

wasTitleInPreviousWeek = function(title, week){
  previousWeek = as.Date(week) - 7
  previousWeekTitles = data[data$published_date == previousWeek,]$title
  result = title %in% previousWeekTitles
  return(result)
}

titlesInListAlready <- c()
submarineTitles <- c()
doubleSubmarineTitles <- c()
counterTotalPositions <- 0
counterSubmarines <- 0
counterDoubleSubmarines <- 0

for(week in weeks){
  print(week)
  titles <- data[data$published_date == week,]$title
  for(title in titles){
    if(title %in% titlesInListAlready && !wasTitleInPreviousWeek(title, week)){
      if(title %in% submarineTitles){
        print("DOUBLE SUBMARINE")
        print(title)
        doubleSubmarineTitles <- c(doubleSubmarineTitles, title)
        submarineTitles <- submarineTitles[submarineTitles!=title]
        counterDoubleSubmarines <- counterDoubleSubmarines + 1
      }
      if(!(title %in% submarineTitles) && !(title %in% doubleSubmarineTitles)){
        print("SUBMARINE")
        print(title)
        submarineTitles <- c(submarineTitles, title)
        counterSubmarines <- counterSubmarines + 1
      }
      
    }
  }
  counterTotalPositions <- counterTotalPositions + length(titles)
  titlesInListAlready <- c(titlesInListAlready, titles)
}

counterTotalPositions
counterSubmarines
counterDoubleSubmarines

submarineTitles
doubleSubmarineTitles
