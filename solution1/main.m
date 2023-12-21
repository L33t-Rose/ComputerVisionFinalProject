% Junior Jean jj37624n@pace.edu Final Project Solution 1
function main
    runall = false;
    if ~runall
        id = "9002430";
        image = readFromID(id);
        processedImage = preprocess(image);
        result = computeTable(processedImage);
        fig = figure;
        imshow(image,[]);
        [r,~] = size(result.BoundingBox);
        hold on;
        for i=1:r
            box = result.BoundingBox(i,1:4);
            % disp([box]);
            drawrectangle('Position',box,'Color','b','Label',sprintf('%d',i),'InteractionsAllowed','none');
        end 
        hold off;
        f = getframe(fig);
        writetable(result,sprintf('./output/%s.csv',id))
        imwrite(f.cdata,sprintf('./output/%s.png',id));
        close all;
    else
        listOfIDs = dir('input_images');
        [rows,numOfChars] = (size(listOfIDs));
        
        whos;
        for idNum= 3:numel(listOfIDs)
            id=listOfIDs(idNum);
            whos;
            disp(id.name);
            image = readFromID(id.name);
            processedImage = preprocess(image);
            result = computeTable(processedImage);
            fig = figure;
            imshow(image,[]);
            [r,~] = size(result.BoundingBox);
            hold on;
            for i=1:r
                box = result.BoundingBox(i,1:4);
                % disp([box]);
                drawrectangle('Position',box,'Color','b','Label',sprintf('%d',i),'InteractionsAllowed','none');
            end 
            hold off;
            f = getframe(fig);
            writetable(result,sprintf('./output/%s.csv',id.name))
            imwrite(f.cdata,sprintf('./output/%s.png',id.name));
            close all;
        end
    end
    disp('----Finished Solution 1-----');
    pause;
    clear all;
    close all;
    
end

% function evaluate

function notHand = calcNotHand(img)
    temp = zeros(size(img));
    figure;
    % imshow(bwpropfilt(imbinarize(imadjust(histeq(img),[],[],0.05),'global'),'Area',[300000 500000]));
    imshow(imbinarize(histeq(img),'global'),[]);
end


function table = computeTable(image)
    image = imdilate(image,strel('diamond',6));
    table = regionprops("table",image,'Centroid','BoundingBox','Area','MajorAxisLength','MinorAxisLength');
    table.Ratio = table.BoundingBox(:,4)./table.BoundingBox(:,3);
    disp('Before');
    disp(table);
    
    avgArea = median(table{:,1});
    table = table(((table.BoundingBox(:,3) > table.BoundingBox(:,4) & (table.Ratio <= 0.75) )),:);
    disp('After');
    disp(table);
    hold off;
end

function img = readFromID(id)
    path = sprintf('./input_images/%s/v06/001',id);
    img = dicomread(dicominfo(path));
end

function newImg = preprocess(img)
    sobelFilter = [2 2 2;0 0 0;-2 -2 -2];
    verticalLineStrel = strel('line',3,90);

    newImg = histeq(img);
    % newImg = histeq(newImg);
    newImg = imfilter(newImg,sobelFilter);
    otsu = otsuthresh(imhist(newImg));
    newImg = imbinarize(newImg,'adaptive','ForegroundPolarity','bright','Sensitivity',otsu); 
    % figure;
    % subplot(1,2,1);
    % imshow(edge(img,'Canny'))
    % imshow(newImg);
    newImg = imerode(newImg,verticalLineStrel);
    
    [r,c] = size(newImg);
    newImg(1:200,:)=0;
    newImg(r/2 + 200:r,:)=0;
    
    % newImg = imclose(newImg,strel("rectangle",[2 6]));
    % newImg = imerode(newImg,strel('square',7));
    % newImg = imerode(newImg,strel('line',5,90));
    % newImg = bwareafilt(newImg,[100 1000],8);
    A = regionprops("table",newImg,'BoundingBox','PixelIdxList','Centroid');
    A=A((A.BoundingBox(:,4) >= A.BoundingBox(:,3)) | ( A.Centroid(:,2) > r/2 + 200),:  );
    newImg(cell2mat(A.PixelIdxList))=0;
    newImg = imdilate(newImg,strel('rectangle',[2 11]));
    newImg = bwareafilt(newImg,[100 2500],8); 
    thing =edge(img,'Canny');
    newImg(thing ~= 1) = 0; 
    
    % subplot(1,2,2);
    % imshow(newImg);
    newImg = bwpropfilt(newImg,'MajorAxisLength',[30 500]);
    % test = A(idx,:);
end