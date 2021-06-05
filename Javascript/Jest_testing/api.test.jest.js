import { describe, it, expect } from "@jest/globals";
import { MyLambdaClient } from "aws-sdk";

const LambdaClient = new MyLambdaClient();

describe("lambda fcn client-config-svc", () => {
  it("GET /api/clients can respond", async () => {
    //Arrange
    const data = new TextEncoder("UTF-8").encode(
      JSON.stringify({
        path: "/client-config-svc//api/clients",
        httpMethod: "GET",
      })
    );
    const expected = ["niagara-wineries"];
    const notExpected = ["testName1", "testName2"];

    //Act
    const response = await LambdaClient.invoke({
      FunctionName: "client-config-svc",
      payload: data,
    });

    //Assert
    expect(response.statusCode).toBe(200);
    expect(typeof response.body).toBe(Array);
    expect(response.body).toEqual(expect.arrayContaining(expected));
    expect(response.body).not.toEqual(expect.arrayContaining(notExpected));
  });

  it("GET /api/clients can respond", async () => {
    //Arrange
    const data = new TextEncoder("UTF-8").encode(
      JSON.stringify({
        path: "/client-config-svc/api",
        httpMethod: "GET",
      })
    );
    //Act
    const response = await LambdaClient.invoke({
      FunctionName: "client-config-svc",
      payload: data,
    });
    //Assert
    expect(response.statusCode).toBe(200);
    expect(response.body).toBe();
  });
});
